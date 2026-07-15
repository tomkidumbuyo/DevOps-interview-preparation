# Networking

<!-- chapter-guide:start -->
> **Step 028 of 373 — 03**
>
> **Builds on:** [Essential Linux commands](../02-linux/12-essential-linux-commands/README.md)
>
> **Now:** Learn **Networking** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [OSI and TCP/IP models](01-osi-and-tcp-ip-models/README.md).
<!-- chapter-guide:end -->

## Packet mental model

Applications write bytes/messages to sockets; transport segments/datagrams them; IP routes packets; links frame them. Encapsulation adds headers and MTU pressure. Every diagnosis should state source/destination address, port, protocol, namespace, expected path, return path and failure phase: name resolution, connect/handshake, TLS, request/response or application.

IPv4/IPv6 CIDR represents prefix length; subnetting allocates address ranges and broadcast domains. Longest-prefix match selects routes. Private addressing is not security. NAT rewrites addresses/ports and requires conntrack/state; it can exhaust ports and obscures identity. IPv6 changes addressing/NAT expectations but still needs routing/firewalling.

At Layer 2, switches forward by MAC, ARP/ND resolves local next hops, VLANs segment broadcast domains and STP prevents loops. At Layer 3, routers use static/dynamic routes; BGP exchanges reachability under policy, not latency promises. ECMP spreads flows across equal-cost paths. Asymmetric routing can break stateful firewalls/NAT.

## TCP, UDP and QUIC

TCP establishes state with SYN/SYN-ACK/ACK, numbers bytes, acknowledges/retransmits, applies receive-window flow control and congestion control. Latency/loss affects throughput; keepalive is not an application health check. `TIME_WAIT` protects old segments; mass outbound connections can exhaust ephemeral ports. UDP has no built-in delivery/order/congestion contract. QUIC provides encrypted multiplexed transport over UDP and moves recovery/streams into user space.

## DNS, HTTP and TLS

Stub resolvers query recursive resolvers, which follow delegation to authoritative servers and cache positive/negative answers by TTL. A/AAAA address, CNAME aliases, MX mail, TXT metadata, NS delegation and SRV service records. Split-horizon views differ by client network; DNSSEC authenticates signed data, not confidentiality. Diagnose application resolver/search/hosts/cache as well as `dig`.

HTTP methods have safety/idempotency semantics, status classes and headers controlling content/auth/cache/connection. HTTP/1.1 reuses connections; HTTP/2 multiplexes streams; HTTP/3 runs over QUIC. WebSockets upgrade to bidirectional messages; SSE streams server events. Align proxy/app timeouts, cancellation and streaming buffering.

TLS negotiates version/cipher/key agreement, validates certificate chain/hostname/time and derives symmetric session keys. SANs identify hosts; SNI selects virtual host/cert; mTLS authenticates both sides. Termination, re-encryption and passthrough have different visibility/trust. Rotate before expiry and verify clients/trust bundles.

## Load balancing, proxies and firewalls

L4 balances connections; L7 routes requests. Algorithms include round robin, least connections, weighted and consistent hashing. Health readiness, draining, stickiness and cross-zone/global distribution determine failure behavior. Forward proxies act for clients; reverse/API gateways act for servers; sidecars/service meshes add per-workload policy/telemetry at complexity cost.

Stateful firewalls remember flows; stateless rules require both directions. SNAT changes source, DNAT destination, PAT ports. Rate limiting protects fairness/quotas; load shedding protects survival; neither is the same as autoscaling.

## Troubleshooting sequence

1. Reproduce from the affected namespace/client and timestamp it.
2. Resolve name through the same resolver path; validate address/family/TTL.
3. Inspect local address, route/rules/neighbor and MTU.
4. Observe handshake with `ss`, `curl -v`, `openssl s_client` and packet capture.
5. Inspect every routing/NAT/firewall/LB/proxy hop and return path.
6. Separate connect, TLS, upstream timeout/reset/status and application saturation.
7. Mitigate reversibly, verify end-to-end and create a synthetic path check.

Common traps: ICMP success does not prove TCP; a listening socket does not prove readiness; DNS may return multiple/family-specific answers; traceroute is not the exact application path; opening a firewall cannot repair missing routes; retries can worsen loss/overload.

## Revision summary

- Follow name → route → filter/NAT → handshake → TLS → HTTP/application → return.
- TCP reliability is scoped to a connection, not end-to-end business success.
- TTL/caches shape DNS failover.
- TLS identity validation is as important as encryption.
- Stateful middleboxes and asymmetric paths are a frequent hidden failure.

## Practice this chapter

Prerequisite: a disposable container network. Create an isolated bridge and a small HTTP server, verify name resolution and a successful request, then test a wrong name, a closed port and one deliberately blocked path. For each failure, distinguish DNS, route, transport and application evidence before changing anything. Treat packet, flow, proxy and application signals as one network observability path. Roll back the rule you added, verify the original client path, remove the named containers and network, and confirm no listener or namespace remains. The harder extension is a packet-path diagram annotated with the exact observation available at each hop.

## Read further

- [RFC Editor](https://www.rfc-editor.org/) — the primary index for Internet standards and RFCs. Follow the specific protocol links in the child chapters and verify whether an RFC is current, updated or obsolete.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Essential Linux commands](../02-linux/12-essential-linux-commands/README.md) · [Questions](questions-and-answers.md) · [Next: OSI and TCP/IP models →](01-osi-and-tcp-ip-models/README.md)

<!-- reading-navigation:end -->
