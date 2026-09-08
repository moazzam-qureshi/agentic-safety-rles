# svc

## Boot

A broken plugin must never stop the service booting. A broken *config*
must always stop it - booting on a bad config is how we ship outages.
