.PHONY: check wordpress publish
check:
	@python3 scripts/check.py

# Rebuild the `wordpress` branch Git It Write publishes from.
wordpress:
	@python3 scripts/wordpress.py

# Check, rebuild `wordpress`, and push main and wordpress to Gitea and GitHub.
publish:
	@scripts/publish.sh
