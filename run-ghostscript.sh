gs -sDEVICE=pngalpha -o output.png -r144 original.pdf | convert -background transparent output.png

convert -background transparent output.png output2.png