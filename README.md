# simple-link-checker

Just pipe URLs to this Docker image.

**Example:**

File `urls.txt`:
```text
http://google.com
https://duckduckgo.com
http://broken-link.tld
```

**Usage:**

`cat urls.txt | docker run --rm -i ovalseven8/simple-link-checker`

**Output:**

```text
HEAD requests have failed for the following URLs:
http://broken-link.tld

Because of misconfigured servers the URLs are checked using GET requests now ...

1/3 are broken:
http://broken-link.tld
```

