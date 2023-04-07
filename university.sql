--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2
-- Dumped by pg_dump version 14.2

-- Started on 2022-04-13 15:30:20 CDT

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
-- TOC entry 209 (class 1259 OID 16435)
-- Name: department_t; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.department_t (
    dept_name character varying(15) NOT NULL,
    building character varying(20) NOT NULL
);


ALTER TABLE public.department_t OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 16440)
-- Name: instructor_t; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.instructor_t (
    i_id character(3) NOT NULL,
    first_name character varying(20) NOT NULL,
    last_name character varying(20) NOT NULL,
    dob date NOT NULL
);


ALTER TABLE public.instructor_t OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 16445)
-- Name: permanent_t; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.permanent_t (
    i_id character(3) NOT NULL,
    office_building character varying(20) NOT NULL,
    office_room character varying(5) NOT NULL,
    salary integer NOT NULL
);


ALTER TABLE public.permanent_t OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 16455)
-- Name: student_t; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_t (
    s_id character(3) NOT NULL,
    first_name character varying(20) NOT NULL,
    last_name character varying(20) NOT NULL,
    dob date NOT NULL,
    dept character varying(15),
    total_credits integer
);


ALTER TABLE public.student_t OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 16450)
-- Name: visiting_t; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.visiting_t (
    i_id character(3) NOT NULL,
    hourly_wage integer NOT NULL
);


ALTER TABLE public.visiting_t OWNER TO postgres;

--
-- TOC entry 3594 (class 0 OID 16435)
-- Dependencies: 209
-- Data for Name: department_t; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.department_t (dept_name, building) FROM stdin;
CS	Stuart
Biology	Hermann
Physics	Kaplan
Engineering	Rettaliata
Music	VanderCook
Science	Pritzker
Business	Stuart
\.


--
-- TOC entry 3595 (class 0 OID 16440)
-- Dependencies: 210
-- Data for Name: instructor_t; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.instructor_t (i_id, first_name, last_name, dob) FROM stdin;
123	Issac	Newton	1951-08-09
456	Albert	Einstein	1958-12-17
789	Nikola	Tesla	1995-04-15
135	Galileo	Galilei	1986-05-14
359	Stephen	Hawking	1964-09-13
759	Charles	Darwin	1987-07-06
246	Thomas	Edison	1973-06-03
286	Michael	Faraday	1953-12-07
913	Michael	Choi	1966-01-01
\.


--
-- TOC entry 3596 (class 0 OID 16445)
-- Dependencies: 211
-- Data for Name: permanent_t; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.permanent_t (i_id, office_building, office_room, salary) FROM stdin;
123	Stuart	112A	80000
789	Rettaliata	012D	90000
359	VanderCook	201B	75000
246	Pritzker	315F	99000
913	Stuart	107C	150000
\.


--
-- TOC entry 3598 (class 0 OID 16455)
-- Dependencies: 213
-- Data for Name: student_t; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_t (s_id, first_name, last_name, dob, dept, total_credits) FROM stdin;
111	Shahrukh	Sohail	1996-01-01	CS	15
222	Peter	Parker	2003-12-07	Biology	9
333	Tony	Stark	1995-04-15	Physics	13
444	Bruce	Banner	1993-06-03	Music	20
555	Steven	Rogers	1964-09-13	CS	7
666	Clinton	Barton	1987-07-06	Engineering	5
777	Victor	Shade	1998-12-17	Physics	33
888	Natasha	Romanoff	1991-08-09	Business	16
999	Clark	Kent	1986-05-14	Science	10
109	Bruce	Wayne	1990-09-25	Engineering	8
108	Diana	Prince	1976-03-17	Biology	3
107	Barry	Allen	2005-10-27	Science	0
105	Oliver	Queen	2002-02-16	Business	28
103	Walter	White	2001-11-24	Music	25
101	Amy	Adams	1999-08-12	CS	18
\.


--
-- TOC entry 3597 (class 0 OID 16450)
-- Dependencies: 212
-- Data for Name: visiting_t; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.visiting_t (i_id, hourly_wage) FROM stdin;
456	35
135	50
759	60
286	45
\.


--
-- TOC entry 3446 (class 2606 OID 16439)
-- Name: department_t department_t_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.department_t
    ADD CONSTRAINT department_t_pkey PRIMARY KEY (dept_name);


--
-- TOC entry 3448 (class 2606 OID 16444)
-- Name: instructor_t instructor_t_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.instructor_t
    ADD CONSTRAINT instructor_t_pkey PRIMARY KEY (i_id);


--
-- TOC entry 3450 (class 2606 OID 16449)
-- Name: permanent_t permanent_t_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permanent_t
    ADD CONSTRAINT permanent_t_pkey PRIMARY KEY (i_id);


--
-- TOC entry 3454 (class 2606 OID 16459)
-- Name: student_t student_t_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_t
    ADD CONSTRAINT student_t_pkey PRIMARY KEY (s_id);


--
-- TOC entry 3452 (class 2606 OID 16454)
-- Name: visiting_t visiting_t_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.visiting_t
    ADD CONSTRAINT visiting_t_pkey PRIMARY KEY (i_id);


-- Completed on 2022-04-13 15:30:21 CDT

--
-- PostgreSQL database dump complete
--

