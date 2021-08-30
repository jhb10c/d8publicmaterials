test = {   'name': 'q1_2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> import numpy as np;\n'
                                               ">>> # It looks like you didn't "
                                               'make an array.;\n'
                                               '>>> type(book_title_words) == '
                                               'np.ndarray\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # It looks like you '
                                               'included commas in the text.;\n'
                                               '>>> # The three pieces of text '
                                               'in the array should be:;\n'
                                               '>>> #   "Eats";\n'
                                               '>>> #   "Shoots";\n'
                                               '>>> #   "and Leaves";\n'
                                               ">>> not any([',' in text for "
                                               'text in book_title_words])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> # It looks like you didn't "
                                               'include both words in the;\n'
                                               '>>> # last piece of text.  It '
                                               'should be the actual string:;\n'
                                               '>>> #   "and Leaves";\n'
                                               ">>> 'and ' in "
                                               'book_title_words.item(2)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> len(book_title_words)\n3',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> book_title_words.item(0) '
                                               "== 'Eats'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> book_title_words.item(1) '
                                               "== 'Shoots'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> book_title_words.item(2) '
                                               "== 'and Leaves'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
