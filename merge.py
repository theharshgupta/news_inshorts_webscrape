fout = open("out.csv", "a", encoding="utf-8")
# first file:
for line in open("data/data0.0.csv", encoding="utf-8"):
    fout.write(line)
# now the rest:
for num in range(1, 60):
    f = open("data/data" + str(num) + ".0" + ".csv", encoding="utf-8")
    f.__next__()
    for line in f:
        fout.write(line)
    f.close()  # not really needed
fout.close()
