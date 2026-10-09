.PHONY: check wordpress
check:
	@python3 scripts/check.py

# Rebuild the `wordpress` branch Git It Write publishes from; push it with
# `git push github wordpress`.
wordpress:
	@python3 scripts/wordpress.py
