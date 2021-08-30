test = {
  'name': 'q36',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> cumming_markets.num_rows == 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(cumming_markets.column('city')) == ['Cumming', 'Cumming']
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
