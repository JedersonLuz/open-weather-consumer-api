--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: cities_weather_request; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cities_weather_request (
    id integer NOT NULL,
    uuid uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    user_id text NOT NULL,
    request_date timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    cities_weather_data json,
    num_cities integer,
    num_progress integer DEFAULT 0,
    status text DEFAULT 'in_progress'::text
);


ALTER TABLE public.cities_weather_request OWNER TO postgres;

--
-- Name: cities-weather-data_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."cities-weather-data_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."cities-weather-data_id_seq" OWNER TO postgres;

--
-- Name: cities-weather-data_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."cities-weather-data_id_seq" OWNED BY public.cities_weather_request.id;


--
-- Name: cities_weather_request id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cities_weather_request ALTER COLUMN id SET DEFAULT nextval('public."cities-weather-data_id_seq"'::regclass);


--
-- Data for Name: cities_weather_request; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cities_weather_request (id, uuid, user_id, request_date, cities_weather_data, num_cities, num_progress, status) FROM stdin;
\.


--
-- Name: cities-weather-data_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."cities-weather-data_id_seq"', 32, true);


--
-- Name: cities_weather_request cities-weather-data_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cities_weather_request
    ADD CONSTRAINT "cities-weather-data_pkey" PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

