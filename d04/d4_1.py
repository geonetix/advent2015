from hashlib import md5

SECRET = "ckczppom"
# Yes, I know this is not infinite, for the purposes of this test, close enough
INFINITE = 10 * (10 ** 8)


def main():
    return ""


def iterate(secret):
    for x in xrange(INFINITE):
        if md5("%s%d" % (secret, x)).hexdigest()[:5] == "00000":
            return x
    print "Max x hit:", x
    return "Not found"


if __name__ == "__main__":
    print "Sanity: abcdef:", iterate("abcdef")
    print "Sanity: pqrstuv:", iterate("pqrstuv")
    print "Code: {}:".format(SECRET), iterate(SECRET)
    main()
