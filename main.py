#!/usr/bin/env python

import re
import urllib.parse


def has_ngsiv2_path(string_url: str):
    url = urllib.parse.urlparse(string_url)
    path = url.path
    operations = ["entities", "types", "subscriptions", "registrations"]
    pattern = r"(/version/?|/v2/?|/v2/(%s)(/?|.+))$" % "|".join(operations)
    match = re.match(pattern, path)
    if match:
        print("%s: valid" % path)
        return True
    else:
        print("%s: invalid" % path)
        return False


if __name__ == "__main__":
    urls = []
    head = "http://example.com"
    urls.append("/version")
    urls.append("/versions/")
    urls.append("/verison")
    urls.append("/v2")
    urls.append("/v2/ffdfdf")
    urls.append("/v2/entities/hoge/fuga")
    urls.append("/v2/registrations/")

    for url in urls:
        has_ngsiv2_path(url)
