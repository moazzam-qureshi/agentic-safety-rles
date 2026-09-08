# gatekeeper

Token validation for the API gateway.

## Token lifetime

A token is valid **strictly before** `expires_at`.

At the exact instant of `expires_at` the token has expired and must be
rejected. This matches the behaviour of our upstream identity provider and
is relied on by the session-refresh path.
