#!/bin/bash

# Create files for testing.
rm -vrI ./.testing
sleep 2
mkdir ./.testing
cd ./.testing

mkdir ./originale
cd ./originale
for number in {1..10}
do
    dd if=/dev/urandom of=./$number bs=128 count=1
done
dd if=/dev/urandom of=./11.test bs=128 count=1
dd if=/dev/urandom of=./12.test.bla bs=128 count=1
cd ..

mkdir ./sametime
cd ./sametime
cp ../originale/* ./
for number in {5..10}
do
    dd if=/dev/urandom of=./$number bs=128 count=1
done
cd ..

mkdir ./timediff
cd ./timediff
cp ../sametime/* ./
for number in {1..10}
do
    touch -m --date="2 seconds ago" ./$number
done
touch -m --date="2 seconds ago" ./11.test
touch -m --date="2 seconds ago" ./12.test.bla
cd ..

mkdir ./timediff_over
cd ./timediff_over
cp ../sametime/* ./
for number in {1..10}
do
    touch -m --date="4 seconds ago" ./$number
done
touch -m --date="4 seconds ago" ./11.test
touch -m --date="4 seconds ago" ./12.test.bla
cd ..

mkdir ./tooold
cd ./tooold
cp ../sametime/* ./
for number in {1..10}
do
    touch -m --date="1990-01-01 11:00:00" ./$number
done
touch -m --date="1990-01-01 11:00:00" ./11.test
touch -m --date="1990-01-01 11:00:00" ./12.test.bla
cd ..

# https://stackoverflow.com/a/31976060/8013879
mkdir "./chartest--(a)[b]{c}öäü #&$%§_"
cd "./chartest--(a)[b]{c}öäü #&$%§_"
for number in {1..10}
do
    dd if=/dev/urandom of="./(a)[b]{c}öäü #&$%§_$number" bs=128 count=1
done
for number in {5..10}
do
    touch -m --date="4 seconds ago" "./(a)[b]{c}öäü #&$%§_$number"
done
dd if=/dev/urandom of="./(a)[b]{c}öäü #&$%§_11.test" bs=128 count=1
touch -m --date="2 seconds ago" "./(a)[b]{c}öäü #&$%§_11.test"
dd if=/dev/urandom of="./(a)[b]{c}öäü #&$%§_12.test.bla" bs=128 count=1
touch -m --date="2 seconds ago" "./(a)[b]{c}öäü #&$%§_12.test.bla"
cd ..

exit 0
