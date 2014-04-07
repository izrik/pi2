
import datetime
import git
import os
import itertools
import string
import argparse

_0 = [0, 1, 1, 1, 1, 1, 0,
      0, 1, 0, 0, 0, 1, 0,
      0, 1, 1, 1, 1, 1, 0]

_1 = [0, 0, 1, 0, 0, 0, 0,
      0, 1, 1, 1, 1, 1, 0,
      0, 0, 0, 0, 0, 0, 0]

_2 = [0, 1, 0, 0, 1, 1, 0,
      0, 1, 0, 1, 0, 1, 0,
      0, 0, 1, 0, 0, 1, 0]

_3 = [0, 1, 0, 0, 0, 1, 0,
      0, 1, 0, 1, 0, 1, 0,
      0, 0, 1, 0, 1, 0, 0]

_4 = [0, 1, 1, 1, 0, 0, 0,
      0, 0, 0, 1, 0, 0, 0,
      0, 0, 1, 1, 1, 1, 0]

_5 = [0, 1, 1, 1, 0, 1, 0,
      0, 1, 0, 1, 0, 1, 0,
      0, 1, 0, 0, 1, 0, 0]

_6 = [0, 0, 1, 1, 1, 1, 0,
      0, 1, 0, 1, 0, 1, 0,
      0, 1, 0, 1, 1, 1, 0]

_7 = [0, 1, 0, 0, 1, 1, 0,
      0, 1, 0, 1, 0, 0, 0,
      0, 1, 1, 0, 0, 0, 0]

_8 = [0, 1, 1, 1, 1, 1, 0,
      0, 1, 0, 1, 0, 1, 0,
      0, 1, 1, 1, 1, 1, 0]

_9 = [0, 1, 1, 1, 0, 1, 0,
      0, 1, 0, 1, 0, 1, 0,
      0, 1, 1, 1, 1, 0, 0]

_dot = [0, 0, 0, 0, 0, 1, 0]

_space = [0, 0, 0, 0, 0, 0, 0]

digit_pixels = [_0, _1, _2, _3, _4, _5, _6, _7, _8, _9]

digits = [1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4,
          3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3,
          7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5]

pixels = _3 + _space + _dot + _space

for digit in digits:
    pixels += digit_pixels[digit] + _space
    if len(pixels) > 367:
        break


def render_date(current_date, seconds):
    d = current_date + datetime.timedelta(hours=3, seconds=seconds)
    return d.strftime('%Y-%m-%dT%H:%M:%S')


def edit_file():
    r = file_data.next()
    with open('file.txt', 'w') as f:
        f.write(r)


def make_commit():
    # repo.index.add(['file.txt'])
    # repo.index.commit('_')
    repo.git.commit('--allow-empty', '-m', '_')


start_year = 2013
start_month = 4
start_day = 14
start_date = datetime.datetime(start_year, start_month, start_day)
file_data = itertools.cycle(string.printable)
repo = git.Repo('.')

def run():
    N = 200
    line = ''
    current_date = start_date
    for p in pixels:

        if p:
            print(render_date(current_date, 0))
            for j in xrange(N):
                datestr = render_date(current_date, j)
                os.environ['GIT_AUTHOR_DATE'] = datestr
                os.environ['GIT_COMMITTER_DATE'] = datestr

                # edit_file()
                make_commit()

        current_date += datetime.timedelta(days=1)


if __name__ == '__main__':
    run()
