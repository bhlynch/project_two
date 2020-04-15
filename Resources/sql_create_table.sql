CREATE TABLE "fire_table"
(
  "fire_id" integer,
  "fire_name" VARCHAR(50),
  "fire_size" FLOAT,
  "STAT_CAUSE_DESCR" VARCHAR ,	
  "latitude" FLOAT,
  "longitude" FLOAT,
  "state_code" VARCHAR,
  "disc_clean_date" DATE,
  "cont_clean_date" DATE,
  "Vegitation" VARCHAR,
  PRIMARY KEY (
	  "fire_id"
  )	
);

SELECT * FROM fire_table



