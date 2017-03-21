********************
xivo-agentd REST API
********************

You can view the API documentation at http://api.wazo.community.

Changelog
=========

17.05
-----

* Add an optional `reason` field to the body of the pause resource.

  * POST /agents/by-number/{agent_number}/pause


15.19
-----

* Token authentication is now required for all routes, i.e. it is not possible to interact with
  xivo-agentd without a xivo-auth authentication token.


15.18
-----

* xivo-agentd now uses HTTPS instead of HTTP.


15.15
-----

* The resources returning agent statuses, i.e.:

  * GET /agents
  * GET /agents/by-id/{agent_id}
  * GET /agents/by-number/{agent_number}

  are now returning an additional argument named "state_interface", which is "the interface (e.g.
  SIP/alice) that is used to determine if an agent is in use or not".
