# Asyncio Streams

> Streams are high-level async/await-ready primitives to work with network connections.

## Client side functions

* `asyncio.open_connection(host=None, port=None, *, loop=None, limit=None, ssl=None, family=0, proto=0, flags=0, sock=None, local_addr=None, server_hostname=None, ssl_handshake_timeout=None)`

* `asyncio.open_unix_connection(path=None, *, loop=None, limit=None, ssl=None, sock=None, server_hostname=None, ssl_handshake_timeout=None)`

Both the functions return a tuple (reader, writer)

## Server side functions

* `asyncio.start_server(client_connected_callback, host=None, port=None, *, loop=None, limit=None, family=socket.AF_UNSPEC, flags=socket.AI_PASSIVE, sock=None, backlog=100, ssl=None, reuse_address=None, reuse_port=None, ssl_handshake_timeout=None, start_serving=True)`

* `asyncio.start_unix_server(client_connected_callback, path=None, *, loop=None, limit=None, sock=None, backlog=100, ssl=None, ssl_handshake_timeout=None, start_serving=True)`

* Both the functions return a handle to the server.
* `client_connected_callback` can be a callable or a coroutine function.

## StreamReader and StreamWriter important methods

* [StreamReader methods](https://docs.python.org/3/library/asyncio-stream.html#streamreader). Some important coroutine functions for reading are `read(n=-1)`, `readline()`, `readexactly(n)`, `readuntil(separator=b'\n')`

* [StreamWriter methods](https://docs.python.org/3/library/asyncio-stream.html#streamwriter). Some important methods for writing are `write(date)` and `writelines(data)`. The pattern is to call the coroutine function  `drain()` after calling any of the write functions. Data to be written should be in either bytes or iterable of bytes.

```Python
# write, writelines,
stream.write(data)
await stream.drain()

# closing the StreamWriter
stream.close()
await stream.wait_closed()
```

---

## References

* [Streams](https://docs.python.org/3/library/asyncio-stream.html)
