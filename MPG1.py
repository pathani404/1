import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))