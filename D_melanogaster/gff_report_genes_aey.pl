#! /usr/bin/perl -w

# gff_report_genes.pl
# take gff spit out genes in specified genomic interval
# Alan E. Yocca
# 02-24-19

use strict;
use Getopt::Long;

my $usage = "\n$0\n" .
			"\t--gff\n" .
				"\t\t<gff input>\n" .
			"\t--chromosome\n" .
				"\t\t<specify which chromosome>\n" . 
				"\t\t<can be comma separated list, matching --interval flag>\n" .
			"\t--interval\n" .
				"\t\t<syntax is <start><colon><stop>>\n" .
				"\t\t<eg. 1:100 for genes from position 1 to 100>\n" .
				"\t\t<if more than 1 chromosome specified,list multiple, separated by commas>\n" .
			"\t--proportion_within\n" .
				"\t\t<only report genes whose specified porportion of their length falls within the given interval>\n" .
				"\t\t<eg 0.5 for reporting genes with at least 50% within the specified interval>\n" .
				"\t\t<default: 0.5>\n" .
				"\t\t<NOT YET FUNCTIONAL 02-25-19>\n" .
			"\t--output\n\n";

my $gff;
my $output;
my @chromosome;
my @interval;
my $proportion_within = 0.5;


GetOptions ( "gff=s" => \$gff,
  "chromosome=s" => \@chromosome,
  "interval=s" => \@interval,
  "proportion_within=s" => \$proportion_within,
  "output=s" => \$output
) or die "$usage\n";
#allows for comma separation
@chromosome = split(/,/,join(',',@chromosome));
@interval = split(/,/,join(',',@interval));


if ( !(defined $gff) || !(defined $output) || ! defined $chromosome[0] || ! defined $interval[0]) {
	die "$usage\n";
}

if (scalar @chromosome != scalar @interval) {
	print "Number of chromosomes and genomic intervals not the same!!\n";
	die "$usage\n";
}
foreach my $interval (@interval) {
	my @start_stop = split(":",$interval);
	if (scalar @start_stop != 2 || $start_stop[1] < $start_stop[0]) {
		print "Interval not split by colon (:), or second coordinate less than start:\n";
		die "$usage\n";
	}
}

open (my $gff_fh, '<', $gff) || die "Cannot open the gff file input: $gff\n\n";
open (my $out_fh, '>', $output) || die "Cannot open the output file: $output\n\n";

my $chromosome="";
my $start;
my $stop;
my $genes;

while (my $line = <$gff_fh>) {
	chomp $line;
	my @line = split("\t",$line);
	next if ($line =~ /^#/ || $line[2] ne "gene" );

	#4       FlyBase gene    879     5039    .       +       .       ID=gene:FBgn0267363;Name=JYalpha;biotype=protein_coding;gene_id=FBgn0267363;logic_name=flybase
	#game plan:
	#if chromosome,
	#hmm matching things...
	#check chromosome, set it
	#set start/stop
	#skip until start
	#skip after stop
	if ($line[0] ne $chromosome) {
		#chromosome either unset, or we moved to a new chromosome
		for (my $i=0; $i < @chromosome; $i++) {
			if ($line[0] eq $chromosome[$i]) {
				#we are on a chromosome that was specified on cmd line
				$chromosome = $chromosome[$i];
				print "set chr: $chromosome\n";
				my @coords = split(":",$interval[$i]);
				$start = $coords[0];
				$stop = $coords[1];
			}
		}
	}
	#lets check if in coords
	#line[3] is gene start
	#line[4] is gene stop
	#skip if either outside interval
	next if ($line[3] > $stop || $line[4] < $start);
	#if completely inside the interval
	if ($line[3] >= $start && $line[4] <= $stop) {
		#print out
		#split gene field
		#example:
		#ID=gene:FBgn0267363;Name=JYalpha;biotype=protein_coding;gene_id=FBgn0267363;logic_name=flybase
		my @field_split = split(";Name",$line[8]);
		my @gene_id = split("ID=",$field_split[0]);
		print $out_fh "$gene_id[1]\n";
		next;
	}

	#if made it here, then only part of the gene is in the interval, need to calculate how much	
#	my $gene_length = $line[4] - $line[3];
	#hmm fastest way to calculate..
###
}

close $gff_fh;
close $out_fh;













