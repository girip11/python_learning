# Concurrency tests

* Run the prepare_input first to generate the required input files
* Run different versions of processing files synchronous, concurrent and parallel versions.
* Multiprocessing version is the fastest. Synchronous, threading and async versions are all atleast 2.5 times slower than the multiprocessing version.

**NOTE**: Async version of reading local files is slower than threading and synchronous version.

---

## References

* [async version runs slower than the non async version](https://stackoverflow.com/questions/60028299/async-version-runs-slower-than-the-non-async-version)
