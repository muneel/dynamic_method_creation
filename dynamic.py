'''
Example to insert methods at runtime based on dictionary
'''

methods = {
    "me": "hello_me",
    "you": "hello_you",
    "him": "hello_who",
    "her": "hello_her",
}


def create_methods(obj):

    def get_name(self, name):
        return name

    def hello_me(*args, **kwargs):
        print "Hello - I am %s !" % get_name(*args)

    def hello_you(*args, **kwargs):
        print "Hello - You are %s!" % get_name(*args)

    def hello_who(*args, **kwargs):
        print "Hello - Who?"

    for k, v in methods.iteritems():
        setattr(obj, k, locals().get(v, hello_who))

    pass


def Dynamic():
    class Dynamic():
        pass

    create_methods(Dynamic)

    return Dynamic()


d = Dynamic()
d.me("John")
d.you("Wayne")
d.him()
d.her()
