comp="abc"
latest=270

for i in {1..270}; do
    x="000${i}"
    num=${x: -3}
    dir=$comp$num
    if [ ! -d $dir ];then
        mkdir $dir
    fi
done