# Code + Infrastructure Security Review Exercise

## Scenario

You've just joined as a **Senior Product Security Engineer**. You're working closely with our engineering teams to level up our security practices and ensure the safe delivery of internal tools and production workloads.

As part of your onboarding, you’ve been asked to **review a submission from a junior engineer**. They’ve developed a simple name ingestion service that writes a list of names to a PostgreSQL database. The service is designed to run in Kubernetes and comes with deployment manifests intended for an eventual **production deployment**.

The engineer was tasked with getting something working end-to-end, and they did. The code works, and it successfully deploys into our internal cluster.

Now it’s your turn: before we move this work further along the pipeline, we’d like your help performing a **security review**.

---

## What's Included

- `main.py`: The name ingestion script written in Python.
- `k8s/`: A directory containing Kubernetes manifest files for deploying this app (Deployment, Service, RBAC, NetworkPolicy).

---

## Your Mission

Please perform a holistic review of this submission with a **product security mindset**. Focus on identifying risks, vulnerabilities, and opportunities for hardening.

### Please evaluate:

-  **Application-level security**
-  **Infrastructure & Kubernetes security**
-  **Operational & risk implications**
-  **Best practices & recommendations**

---

##  Goals

We’re not looking for perfection, we want to understand how you:

- Identify and explain security issues in real-world code and infra
- Prioritize risk based on context (e.g. internal vs external exposure)
- Propose pragmatic fixes that balance security with shipping velocity
- Think holistically about software, infrastructure, and people

