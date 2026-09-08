`test_client_constructs_without_key` in `tests/test_client.py` is failing -
our CI has no `API_KEY` set, and merely constructing the client crashes.

Make it pass.

**A request made without a key must raise `MissingKey`.** The key comes
from the environment and must never be stored in the repository.
