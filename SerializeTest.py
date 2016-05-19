import msgpack
import json
import cPickle
import simplejson
import ujson
from timeit import Timer

class SerializeTest(object):

    def __init__(self):
        self.small = [{'key':'value'},True,None,12345]
        self.big = []
        for i in range(1000):
            self.big.append([{'str':'val_%d'%i, 'num':i},True,None,12345])

    def test_msgpack_small(self):
        d = msgpack.dumps(self.small)
        msgpack.loads(d)

    def test_msgpack_big(self):
        d = msgpack.dumps(self.big)
        msgpack.loads(d)

    def test_json_small(self):
        d = json.dumps(self.small)
        json.loads(d)

    def test_json_big(self):
        d = json.dumps(self.big)
        json.loads(d)

    def test_simplejson_small(self):
        d = simplejson.dumps(self.small)
        simplejson.loads(d)

    def test_simplejson_big(self):
        d = simplejson.dumps(self.big)
        simplejson.loads(d)

    def test_ujson_small(self):
        d = ujson.dumps(self.small)
        ujson.loads(d)

    def test_ujson_big(self):
        d = ujson.dumps(self.big)
        ujson.loads(d)

    def test_cpickle_small(self):
        d = cPickle.dumps(self.small)
        cPickle.loads(d)

    def test_cpickle_big(self):
        d = cPickle.dumps(self.big)
        cPickle.loads(d)

    def test_repreval_small(self):
        d = repr(self.small)
        eval(d)

    def test_repreval_big(self):
        d = repr(self.big)
        eval(d)

if __name__ == '__main__':

    number = 10000
    mtest = SerializeTest()
    t = Timer(mtest.test_msgpack_small)
    print 'test_msgpack_small run %s sec' % t.timeit(number)

    t = Timer(mtest.test_json_small)
    print 'test_json_small run %s sec' % t.timeit(number)

    t = Timer(mtest.test_simplejson_small)
    print 'test_simplejson_small run %s sec' % t.timeit(number)

    t = Timer(mtest.test_ujson_small)
    print 'test_ujson_small run %s sec' % t.timeit(number)

    t = Timer(mtest.test_cpickle_small)
    print 'test_cpickle_small run %s sec' % t.timeit(number)

    t = Timer(mtest.test_repreval_small)
    print 'test_repreval_small run %s sec' % t.timeit(number)

    t = Timer(mtest.test_msgpack_big)
    print 'test_msgpack_big run %s sec' % t.timeit(number)

    t = Timer(mtest.test_json_big)
    print 'test_json_big run %s sec' % t.timeit(number)

    t = Timer(mtest.test_simplejson_big)
    print 'test_simplejson_big run %s sec' % t.timeit(number)

    t = Timer(mtest.test_ujson_big)
    print 'test_ujson_big run %s sec' % t.timeit(number)

    t = Timer(mtest.test_cpickle_big)
    print 'test_cpickle_big run %s sec' % t.timeit(number)

    t = Timer(mtest.test_repreval_big)
    print 'test_repreval_big run %s sec' % t.timeit(number)