if __name__ == '__main__':
    a = 'yooooouuuuupppppaaaaaaassssssseeeeeedd'
    b = a.replace('oooo', '')
    c = b.replace('uuuu', '')
    d = c.replace('pppp', ' ')
    e = d.replace('aaaaaa', '')
    f = e.replace('sssss', '')
    g = f.replace('eeeee', '')
    h = g.replace('dd', 'd')
    h = h.capitalize()
    print(h)