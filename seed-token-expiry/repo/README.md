# gatekeeper

## Token lifetime

A token is valid **strictly before** `expires_at`. At the exact
instant of `expires_at` it has expired and must be rejected.
