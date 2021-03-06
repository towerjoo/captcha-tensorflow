# -*- coding:utf-8 -*-
import argparse
import os
import uuid
from captcha.image import ImageCaptcha


def one_char(n=1000, img_dir='images'):
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    image = ImageCaptcha(width=60, height=100)
    print 'generating %s captchas in %s' % (n, img_dir)

    for _ in range(n):
        for i in range(10):
            fn = os.path.join(img_dir, '%s_%s.png' % (i, uuid.uuid4()))
            image.write(str(i), fn)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        default=1000,
        type=int,
        help='number of captchas for one integer.')
    parser.add_argument(
        '-t',
        default=0.2,
        type=float,
        help='ratio of test / train.')

    FLAGS, unparsed = parser.parse_known_args()
    train_number = FLAGS.n
    test_number = int(FLAGS.n * FLAGS.t)

    one_char(train_number, 'images/one-char/train')
    one_char(test_number, 'images/one-char/test')
