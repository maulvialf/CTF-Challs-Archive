--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: gallery; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gallery (
    id integer NOT NULL,
    name character varying,
    image_path character varying,
    description character varying,
    visible boolean
);


ALTER TABLE public.gallery OWNER TO postgres;

--
-- Name: gallery_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.gallery_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gallery_id_seq OWNER TO postgres;

--
-- Name: gallery_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.gallery_id_seq OWNED BY public.gallery.id;


--
-- Name: user_person; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_person (
    id integer NOT NULL,
    username character varying,
    password character varying,
    email character varying,
    is_admin boolean,
    is_super_admin boolean,
    image character varying,
    time_created timestamp with time zone DEFAULT now(),
    time_updated timestamp with time zone
);


ALTER TABLE public.user_person OWNER TO postgres;

--
-- Name: user_person_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_person_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_person_id_seq OWNER TO postgres;

--
-- Name: user_person_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_person_id_seq OWNED BY public.user_person.id;


--
-- Name: gallery id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gallery ALTER COLUMN id SET DEFAULT nextval('public.gallery_id_seq'::regclass);


--
-- Name: user_person id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_person ALTER COLUMN id SET DEFAULT nextval('public.user_person_id_seq'::regclass);


--
-- Data for Name: gallery; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.gallery (id, name, image_path, description, visible) FROM stdin;
1	Sunset	public/Sunset.jpg	Indah sekali bukan melihat pemandangan sunset ditambah para burung yang berirama dan gunung yang memaku	t
2	Moon	public/Moon.jpg	Bulan memanglah sangat indah, namun apakah pernah terpikir ia selalu kesepian? Apa karena sepi itulah yang membuat dia indah? Atau ada hal yang membuat dia menjadi indah?	t
3	Railroad	public/Railroad.jpg	Perjalanan jauh membuat seseorang melupakan masalahnya, namun apakah ini sebuah jalan pintas kabur dari masalah? atau membuat dia akan menjadi lebih kuat ketika dia kembali untuk menghadapi masalah?	t
4	Sea	public/Sea.jpg	Laut dan Langit adalah hal yang indah namun sulit untuk dicapai, misteri didalamnya pun sangatlah banyak, membuktikan cinta dalam pandangan pertama itu ada	t
5	Forest	public/Forest.jpg	Kesegaran dan Ketenangan adalah hal yang selalu diberikan hutan, namun masih banyak hal lainnya bukan? Tapi kita tetap selalu menjelajahinya tanpa melihat hal lainnya	t
6	Tree	public/Tree.jpg	Pohon adalah inti dari kehidupan namun masih banyak orang yang menyepelakan, saat kehilangan baru ia akan tersadarkan, bahwa sesuatu yang utama akan meninggalkan suasana	t
\.


--
-- Data for Name: user_person; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_person (id, username, password, email, is_admin, is_super_admin, image, time_created, time_updated) FROM stdin;
1	superC0ol	\\x4e4459304d5452694e4455315a6a55774e5463304e413d3d	fake-admin@photograph-app.id	t	t	public/example.svg	2023-05-18 19:35:37.675561+00	2023-05-18 19:35:37.675561+00
\.


--
-- Name: gallery_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.gallery_id_seq', 6, true);


--
-- Name: user_person_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_person_id_seq', 1, true);


--
-- Name: gallery gallery_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gallery
    ADD CONSTRAINT gallery_pkey PRIMARY KEY (id);


--
-- Name: user_person user_person_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_person
    ADD CONSTRAINT user_person_pkey PRIMARY KEY (id);


--
-- Name: ix_gallery_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_gallery_id ON public.gallery USING btree (id);


--
-- Name: ix_user_person_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_user_person_id ON public.user_person USING btree (id);


--
-- PostgreSQL database dump complete
--

