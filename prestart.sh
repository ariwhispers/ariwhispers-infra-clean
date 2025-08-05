#!/usr/bin/env bash
        set -e
        echo '⏳ Pre-start…'; alembic upgrade head || echo 'No DB – skipping'
        exec "$@"
