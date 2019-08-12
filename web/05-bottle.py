import bottle


@bottle.route('/')
def home_page():
    mythings = ['Python', 'Ruby', 'Pearl', 'C++']
    return bottle.template('hello_world', {'username': 'Bonbisu', 'things': mythings})


bottle.debug(True)
bottle.run(host='localhost', port=8082)
