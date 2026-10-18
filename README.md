# Erick Hernández Zenil

Operational excellence for manufacturing, and a home lab I run like a plant.

I spent years on factory floors in Europe, USA, Latinamerica & the Middle East: cost of poor quality, line capacity, idea management, Industry 4.0 pilots that actually scale. In 2024 I founded **[Zenilify Consulting](https://zenilify-consulting.com)** (Toluca · Mexico City · remote) to do that work for mid-sized manufacturers. **[Kaizen Lab](https://kaizen-lab.dev)** is its technical side: a home lab built in public with a lean mindset, where I test self-hosting, local AI, smart-home and DIY hardware on real gear before I recommend any of it.

## The lab, measured in public

**[kaizen-lab.io](https://kaizen-lab.io)** shows the lab as a process, with the numbers a plant manager would ask for: uptime and backups, AI renders, PDCA cycles, an idea funnel (raised → implemented), right-first-time, cost of poor quality, make vs buy. The feed updates every 15 minutes from the lab itself. The same site hosts the calculators I use in client work (OEE, takt time, make-or-buy, bakery line capacity) and a few plant-floor stories, all names removed.

What the lab runs on: two sites joined by Tailscale, Proxmox with about 45 LXC guests, a Synology NAS, an RTX 5090 node for local AI (Ollama, ComfyUI, voice), Home Assistant, Uptime Kuma, n8n, Nextcloud, and a fleet of ESP32 and M5Stack devices. Each change goes through the same loop as a kaizen on the floor: measure, change, verify, record the lessons (the lab keeps a numbered list of its own mistakes, and reads it before repeating one).

## Public repos

| Repo | What it is |
|---|---|
| [kaizen-lab-io](https://github.com/zenilify/kaizen-lab-io) | The KPI board and lean calculators. Static site, Cloudflare Pages, no framework. MIT for the code. |
| [electronics-learning](https://github.com/zenilify/electronics-learning) | My step-by-step notes learning electronics with dev boards: breadboards, soldering, ESP32, XIAO, voice-satellite builds. |

The rest of the lab (runbooks, device registry, workers, skills for Claude) lives in private repos. Ask if something there would help you.

## Writing

- **[zenilify.medium.com](https://zenilify.medium.com)**, in *The Repo*: one build at a time, with the measurements. Recent: turning a 52×16-pixel clock into a home-lab cockpit (Ulanzi TC002).
- Instagram **[@zenilify.kaizenhomelab](https://www.instagram.com/zenilify.kaizenhomelab/)** · X **[@kaizenhomelab](https://x.com/kaizenhomelab)**

## Working with me

- **Diagnóstico gratuito**, 30 minutes on your process: [zenilify-consulting.com/agenda](https://zenilify-consulting.com/agenda/) (EN: [/en/book/](https://zenilify-consulting.com/en/book/)).
- Languages: Spanish, English, German.
- Zenilify Consulting, S.A.P.I. de C.V., is a member of NVIDIA Inception.
