import os.path
import logging

from django.core.mail import send_mail
from PIL import Image

logger = logging.getLogger(__name__)


def generate_thumbnail(image_path, size):
    width, height = size
    logger.info("Generating a {}x{} thumbnail for {}".format(width, height, image_path))
    file, ext = os.path.splitext(image_path)
    im = Image.open(image_path)
    im.thumbnail(size)
    filename = "{}.thumbnail.{}x{}{}".format(file, width, height, ext)
    im.save(filename, "JPEG")


def send_email(to, from_email, subject, text):
    send_mail(subject, text, from_email, [to])
