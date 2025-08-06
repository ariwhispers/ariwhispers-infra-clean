#!/usr/bin/env bash
        set -e
        echo 'â³ Pre-startâ€¦'; alembic upgrade head || echo 'No DB â€“ skipping'
        exec "$@"
