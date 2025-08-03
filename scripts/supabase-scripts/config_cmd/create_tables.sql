CREATE TABLE negative (
    img_url TEXT
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMPTZ
);

CREATE TABLE images (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    image_url TEXT,
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE positive_images (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    image_url TEXT,
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Copy these code into Supabase SQL tool