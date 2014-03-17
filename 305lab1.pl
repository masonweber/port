######################################### 	
#    CSCI 305 - Programming Lab #1		
#										
#  Mason Weber			
#  redwall_runner@hotmail.com			
#										
#########################################

# Replace the string value of the following variable with your names.
my $name = "Mason Weber";
my $partner = "himself only";#no partner
print "CSCI 305 Lab 1 submitted by $name and $partner.\n\n";

# Checks for the argument, fail if none given
if($#ARGV != 0) {
    print STDERR "You must specify the file name as the argument.\n";
    exit 4;
}

# Opens the file and assign it to handle INFILE
open(INFILE, $ARGV[0]) or die "Cannot open $ARGV[0]: $!.\n";


# YOUR VARIABLE DEFINITIONS HERE...
my $count = 0;
my %model;

# This loops through each line of the file
while($line = <INFILE>) {

	# This prints each line. You will not want to keep this line.
	#print $line;
	#regex1, get song data
	$line =~ m/<SEP>.*<SEP>.*<SEP\>(.*)\n/;
	$line = $1;
		
	#regex2
	#selects all text after the first illegal character and replaces it with blank, deleting it.
	$line =~ s/\(.*|\[.*|{.*|\\.*|\/.*|_.*|-.*|:.*|".*|`.*|\+.*|=.*|feat\..*//; 
	
	#regex3
	#selects all remaining single unwanted characters and replaces them with nothing, deleting
	$line =~ s/\?|¿|!|¡|\.|;|&|\$|\@|%|#|\|//g;
	
	#regex4
	#eliminate titles with nonword characters in them
	if ($line =~ m/'/) {#allowing for contractions, else next expression eliminates all
		$count++;
		#print "$line \n";
	} elsif ($line =~ m/(?=\W)(?=\S)/) {#remove lines with a character that is non-word and non-space
		$line = ''; #effective delete
	} else {#standard english song title
		$count++;
		#print "$line \n";
	}
	
	#manipulation 5
	#make $line lower case
	$line = lc($line);
	#print"$line\n";
	
	#regex6
	#removing stop words
	#looks for non word characters on each side, either space or return feed to not get fragments of words that contain 'a' for example
	$line =~ s/\Wa\W|\Wan\W|\Wand\W|\Wby\W|\Wfor\W|\Wfrom\W|\Win\W|\Wof\W|\Won\W|\Wor\W|\Wout\W|\Wthe\W|\Wto\W|\Wwith\W//g;
	
	#build bigram model
	my $word1, $word2;
	while ($line =~ m/(\w+)\s(\w+)/) {
		$word1 = $1;
		$word2 = $2;
		$model{$word1}{$word2}++;
		#print "$word1, $word2, $model{$word1}{$word2}\n";
		$line =~ s/$word1//;
	}
	
}

# Close the file handle
close INFILE; 
print "$count titles processed\n";

# At this point (hopefully) you will have finished processing the song 
# title file and have populated your data structure of bigram counts.
print "File parsed. Bigram model built.\n\n";


# User control loop
print "Enter a word [Enter 'q' to quit]: ";
$input = <STDIN>;
chomp($input);
print "\n";	
while ($input ne "q"){
	$count = 1;
	my $currentWord = $input; #isolate variable to protect $input
	my $title = $currentWord; #start title of some
	while ($count <= 20) {#title length is max 20 words, start at 1		
		my $nextWord = mcw($currentWord); #get next word in title
		$title = $title . ' ' . $nextWord; #concatonate
		$currentWord = $nextWord; 
		$count++;
	}
	print "$title\n";
	$input = <STDIN>; #to keep looping
	chomp($input); #remove newline
}

sub mcw {#most common word function
	my $nextWord = "";
	my $maxCount = 0;
	foreach my $word2 (keys %{ $model{$_[0]} }) {#go through all words following $input, pick max
		if ($model{$_[0]}{$word2} > $maxCount) {#count of current key larger than prev max
			$maxCount = $model{$_[0]}{$word2};
			$nextWord = $word2;
		} elsif ($model{$_[0]}{$word2} > $maxCount) {#counts are equal, need to rand() to break tie
			if (rand() > 0.5) {
				$nextWord = $word2; #update word, leave count same
			}
		}
	}
	return $nextWord;
}