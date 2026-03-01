# EuroHealth AI Helpdesk — Dockerfile
# AI-SE designs this component
#
# Key decisions:
#   - Base image (Python 3.11+ with CUDA for on-prem LLM?)
#   - Multi-stage build for smaller production image
#   - Policy files copied into container at build time
#   - Health check endpoint
#   - Environment-specific config (dev/staging/prod)

# FROM python:3.11-slim
# TODO: AI-SE designs the full Dockerfile
