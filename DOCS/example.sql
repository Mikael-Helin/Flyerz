-- For illustrative purposes only. Not intended for production use.
-- Keep it for PostgreSQL in case for future reference.

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    display_name VARCHAR(100) NOT NULL,
    true_name VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    profile_picture_url VARCHAR(255) DEFAULT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    validated_at TIMESTAMP DEFAULT NULL,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE friends (
    id SERIAL PRIMARY KEY,
    user1_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    user1_accepted TIMESTAMP DEFAULT NULL,
    user2_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE, 
    user2_accepted TIMESTAMP DEFAULT NULL,
    UNIQUE (user1_id, user2_id),
    CHECK (user1_id < user2_id)
);

CREATE TABLE organization_tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE organizations (
    id SERIAL PRIMARY KEY,
    owner_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL UNIQUE, --  Should we have unique here?
    picture_url VARCHAR(255) DEFAULT NULL,
    contact_details TEXT DEFAULT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE organization_tag_mappings (
    organization_id INT NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    tag_id INT NOT NULL REFERENCES organization_tags(id) ON DELETE CASCADE,
    PRIMARY KEY (organization_id, tag_id)
);

CREATE TABLE organization_links (
    organization_id INT NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    name VARCHAR(50) NOT NULL,
    url VARCHAR(255) NOT NULL,
    PRIMARY KEY (organization_id, url)
);

CREATE TABLE organization_followers (
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    organization_id INT NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, organization_id)
);

CREATE TABLE flyer_tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE flyerz (
    id SERIAL PRIMARY KEY,
    entity_id INT REFERENCES organizations(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    event_date DATE,
    price DECIMAL(10, 2),
    is_visible BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (entity_id, name, event_date)
);

CREATE TABLE flyer_tag_mappings (
    flyer_id INT NOT NULL REFERENCES flyerz(id) ON DELETE CASCADE,
    tag_id INT NOT NULL REFERENCES flyer_tags(id) ON DELETE CASCADE,
    PRIMARY KEY (flyer_id, tag_id)
);

CREATE TABLE flyer_attendants (
    flyer_id INT REFERENCES flyerz(id) ON DELETE CASCADE,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (flyer_id, user_id)
);
