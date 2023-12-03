CREATE DATABASE yuniqua;

\c yuniqua;


--- YUNIQUA.EDITOR_USER TABLE 
CREATE TABLE IF NOT EXISTS yuniqua_user (
    user_id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    alias TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL
);


--- YUNIQUA.EDITOR_STATE TABLE
-- DEFAULT = ['ACTIVE', 'ARCHIVED']
CREATE TABLE IF NOT EXISTS editor_state (
    editor_state_id INTEGER PRIMARY KEY,
    name TEXT,
    label TEXT
);

INSERT INTO editor_state (editor_state_id, name, label) 
VALUES (1, 'ACTIVE', 'Active'),
       (2, 'ARCHIVED', 'Archived');


-- YUNIQUA.SUPPORTED_LANGUAGES TABLE 
-- DEFAULT = ['PYTHON', 'C++', 'JAVASCRIPT']
CREATE TABLE IF NOT EXISTS supported_language (
    supported_language_id INTEGER PRIMARY KEY,
    name TEXT,
    label TEXT
);

INSERT INTO supported_language (supported_language_id, name, label) 
VALUES (1, 'PYTHON', 'Python'),
       (2, 'C++', 'C++'),
       (3, 'JAVASCRIPT', 'Javascript');


-- YUNIQUA.SESSION_EDITOR TABLE 
CREATE TABLE IF NOT EXISTS session_editor (
    session_editor_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    access_token TEXT NOT NULL,
    max_connections INTEGER NOT NULL,
    user_owner_id INTEGER NOT NULL REFERENCES yuniqua_user(user_id) ON DELETE CASCADE,
    language_id INTEGER NOT NULL REFERENCES supported_language(supported_language_id) ON DELETE CASCADE,
    state_id INTEGER NOT NULL REFERENCES editor_state(editor_state_id) ON DELETE CASCADE,
    created_at TIMESTAMP NOT NULL
);
