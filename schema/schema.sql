-- anime_entries (staging)
CREATE TABLE IF NOT EXISTS staging_anime (
    staging_id SERIAL PRIMARY KEY,
    platform VARCHAR(10) NOT NULL,  -- 'MAL' or 'AniList'
    external_id VARCHAR(20) NOT NULL,
    title VARCHAR(255) NOT NULL,
    episodes INT,
    score DECIMAL(3,1),
    status VARCHAR(20),
    progress INT,
    platform_specific JSONB
);

-- Comparison results
CREATE TABLE IF NOT EXISTS migration_delta (
    delta_id SERIAL PRIMARY KEY,
    source_id INT REFERENCES staging_anime(staging_id),
    target_id INT REFERENCES staging_anime(staging_id),
    action_needed VARCHAR(20)  -- 'ADD', 'UPDATE', 'CONFLICT'
);
