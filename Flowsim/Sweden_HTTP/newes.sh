#!/usr/bin/gnuplot -persist

set terminal pdf
set output 'sw.pdf'
set logscale x 10
set tics in
set xlabel "Download[ms]" font 'sans-serif,20'
set ylabel 'ECDF' font 'sans-serif,20'
set key bottom
plot 'HTTP3.dat' u 1:2 w l lw 2 lt rgb "#AA151B" title 'HTTP3', 'HTTPS.dat' u 1:2 w l lw 2 lt rgb "#F1BF00" title 'HTTPS', 'HTTP.dat' u 1:2 w l lw 2 lt rgb "#0039F0" title "HTTP"
