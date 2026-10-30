"""
================================================================================
YOTTAFLEX AI RECRUITMENT DRIVE - CANDIDATE CHALLENGE SUBMISSION
Project: Deterministic Relational Data Engine & ATS Workflow Simulator
Author: puchalapalli masthan (pmasthan00@gmail.com)
Target Window: 72 Hours Code Challenge
================================================================================
"""

import os
import random
import datetime
import hashlib
import logging
from typing import Dict, List, Tuple
import pandas as pd
import numpy as np

# Initialize streaming log configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("YottaFlex_Data_Engine")


class ATSDatasetGenerator:
    """
    Modular transaction data generator enforcing relational completeness,
    deterministic reproducible tracking, and isolated anomaly injection matrices.
    """
    def __init__(self, scale_factor: float = 1.0, seed: int = 20261022):
        self.scale_factor = scale_factor
        self.seed = seed
        self.base_date = datetime.datetime(2026, 1, 1)
        
        # Linear scaling distribution parameters
        self.num_reqs = int(100 * scale_factor)
        self.num_candidates = int(2000 * scale_factor)
        self.num_apps_target = int(3000 * scale_factor)
        self.num_interviews_target = int(600 * scale_factor)
        self.num_offers_target = int(150 * scale_factor)
        
        self.ground_truth_records: List[Dict[str, str]] = []
        self._synchronize_state_seeds()

    def _synchronize_state_seeds(self) -> None:
        """Locks cross-library entropy pools to guarantee exact checksum matches."""
        random.seed(self.seed)
        np.random.seed(self.seed)

    @staticmethod
    def calculate_dataframe_checksum(df: pd.DataFrame) -> str:
        """Computes structural SHA-256 data block matrices tokens."""
        hash_array = pd.util.hash_pandas_object(df, index=False).values
        return hashlib.sha256(hash_array).hexdigest()

    def generate_master_directories(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        logger.info("Generating Step 1 Core System Master Data...")
        depts = ["Engineering", "Product Management", "Data Science", "Design", "Operations", "Sales"]
        df_dept = pd.DataFrame({
            "dept_id": [f"DEPT-{i+1:03d}" for i in range(len(depts))],
            "dept_name": depts
        })
        skills = ["Python", "Java", "Go", "SQL", "Machine Learning", "System Design", "Product Strategy", "UI/UX", "Kubernetes", "AWS"]
        df_skill = pd.DataFrame({
            "skill_id": [f"SKILL-{i+1:03d}" for i in range(len(skills))],
            "skill_name": skills
        })
        return df_dept, df_skill

    def generate_job_requisitions(self, df_dept: pd.DataFrame) -> pd.DataFrame:
        logger.info(f"Generating {self.num_reqs} deterministic Job Requisitions...")
        roles = ["Software Engineer", "Data Scientist", "Product Manager", "UX Designer", "DevOps Engineer"]
        dept_ids = df_dept["dept_id"].tolist()
        records = []
        for i in range(self.num_reqs):
            req_id = f"REQ-2026-{i+1:06d}"
            min_sal = random.randint(60000, 110000)
            max_sal = min_sal + random.randint(25000, 55000)
            status = "OPEN" if i < (self.num_reqs - 10) else "CLOSED"
            records.append({
                "requisition_id": req_id, "title": random.choice(roles), "dept_id": random.choice(dept_ids),
                "min_salary": float(min_sal), "max_salary": float(max_sal), "status": status
            })
        return pd.DataFrame(records)

    def generate_candidates(self, df_skill: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
        logger.info(f"Modeling {self.num_candidates} Candidate core matrices...")
        f_names = ["Amit", "Priya", "Rahul", "Neha", "Vijay", "Ananya", "Rajesh", "Kiran", "Suresh", "Lakshmi"]
        l_names = ["Sharma", "Verma", "Kumar", "Singh", "Patel", "Reddy", "Nair", "Joshi", "Das", "Mehta"]
        skill_ids = df_skill["skill_id"].tolist()
        cand_rec, bridge_rec = [], []
        for i in range(self.num_candidates):
            cand_id = f"CAND-{i+1:06d}"
            name = f"{random.choice(f_names)} {random.choice(l_names)}"
            email = f"{name.lower().replace(' ', '')}{i}@synthetic-drive.io"
            cand_rec.append({"candidate_id": cand_id, "full_name": name, "email": email})
            for sk_id in random.sample(skill_ids, random.randint(2, 4)):
                bridge_rec.append({"candidate_id": cand_id, "skill_id": sk_id})
        return pd.DataFrame(cand_rec), pd.DataFrame(bridge_rec)

    def generate_applications(self, df_req: pd.DataFrame, df_cand: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
        logger.info("Assembling structural Candidate Applications entries...")
        req_ids = df_req["requisition_id"].tolist()
        cand_ids = df_cand["candidate_id"].tolist()
        app_rec, res_rec = [], []
        seen = set()
        res_counter = 1
        while len(app_rec) < self.num_apps_target - 5:
            r_id, c_id = random.choice(req_ids), random.choice(cand_ids)
            if (r_id, c_id) not in seen:
                seen.add((r_id, c_id))
                app_id = f"APP-{r_id}-{c_id}"
                days = random.randint(1, 150)
                applied_date = self.base_date + datetime.timedelta(days=days)
                p = random.random()
                status = "SCREENING_FAILED" if p < 0.45 else "WITHDRAWN" if p < 0.60 else "INTERVIEW_STAGE" if p < 0.85 else "OFFER_EXTENDED"
                app_rec.append({
                    "application_id": app_id, "requisition_id": r_id, "candidate_id": c_id,
                    "status": status, "applied_date": applied_date
                })
                res_rec.append({
                    "resume_id": f"RES-{res_counter:06d}", "application_id": app_id,
                    "parsed_text_summary": f"Extracted text profile for structural evaluation ID reference: {app_id}"
                })
                res_counter += 1
        return pd.DataFrame(app_rec), pd.DataFrame(res_rec)

    def generate_interviews_and_feedback(self, df_app: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        logger.info("Mapping Panel Interviews and structured evaluation logs...")
        names = ["Erlang Shen", "Ada Lovelace", "Alan Turing", "Grace Hopper", "Linus Torvalds"]
        df_intv = pd.DataFrame([{"interviewer_id": f"INTV-{i+1:06d}", "name": n, "is_available": True} for i, n in enumerate(names)])
        int_rec, fb_rec = [], []
        apps = df_app[df_app["status"].isin(["INTERVIEW_STAGE", "OFFER_EXTENDED"])].to_dict("records")
        intv_ids = df_intv["interviewer_id"].tolist()
        int_counter = 1
        for _ in range(self.num_interviews_target - 5):
            if not apps: break
            app = random.choice(apps)
            int_id = f"INT-2026-{int_counter:06d}"
            intv_id = random.choice(intv_ids)
            sched = app["applied_date"] + datetime.timedelta(days=random.randint(5, 12))
            int_rec.append({
                "interview_id": int_id, "application_id": app["application_id"],
                "interviewer_id": intv_id, "scheduled_time": sched, "round_number": random.randint(1, 3)
            })
            fb_rec.append({
                "feedback_id": f"FB-{int_id}-{intv_id}", "interview_id": int_id, "interviewer_id": intv_id,
                "score": random.randint(3, 5), "comments": "Passes engineering operational assessment boundaries."
            })
            int_counter += 1
        return df_intv, pd.DataFrame(int_rec), pd.DataFrame(fb_rec)

    def generate_offers(self, df_app: pd.DataFrame, df_req: pd.DataFrame) -> pd.DataFrame:
        logger.info("Drafting transactional onboarding Offers matrix...")
        records = []
        apps = df_app[df_app["status"] == "OFFER_EXTENDED"].to_dict("records")
        req_map = df_req.set_index("requisition_id").to_dict("index")
        counter = 1
        for _ in range(self.num_offers_target - 5):
            if not apps: break
            app = random.choice(apps)
            bounds = req_map.get(app["requisition_id"], {"min_salary": 70000.0, "max_salary": 120000.0})
            off_id = f"OFF-2026-{counter:06d}"
            sal = float(random.randint(int(bounds["min_salary"]), int(bounds["max_salary"])))
            records.append({
                "offer_id": off_id, "application_id": app["application_id"], "salary_offered": sal,
                "is_approved": True, "status": random.choice(["ACCEPTED", "REJECTED"])
            })
            counter += 1
        return pd.DataFrame(records)

    def inject_required_edge_scenarios(self, dfs: Dict[str, pd.DataFrame]) -> None:
        logger.warning("Injecting explicit compliance anomalies into output pipelines...")
        
        # --- Scenario A: Interview scheduled for unavailable interviewer ---
        dfs["interviewers"].loc[dfs["interviewers"]["interviewer_id"] == "INTV-000001", "is_available"] = False
        app_a = dfs["applications"].iloc[0]["application_id"]
        id_a = "INT-2026-999001"
        dfs["interviews"] = pd.concat([dfs["interviews"], pd.DataFrame([{
            "interview_id": id_a, "application_id": app_a, "interviewer_id": "INTV-000001",
            "scheduled_time": datetime.datetime(2026, 8, 15, 10, 0), "round_number": 1
        }])], ignore_index=True)
        self.ground_truth_records.append({"entity_id": id_a, "anomaly_type": "INTERVIEW_UNAVAILABLE_INTERVIEWER", "description": "Scheduled against unallocated panel resource track."})

        # --- Scenario B: Candidate records an explicit Duplicate Submission ---
        c_b = dfs["candidates"].iloc[0]["candidate_id"]
        r_b = dfs["job_requisitions"].iloc[0]["requisition_id"]
        id_b = f"APP-{r_b}-{c_b}-DUP"
        dfs["applications"] = pd.concat([dfs["applications"], pd.DataFrame([{
            "application_id": id_b, 
            "requisition_id": r_b, 
            "candidate_id": c_b,
            "status": "APPLIED", 
            "applied_date": datetime.datetime(2026, 9, 1)
        }])], ignore_index=True)
        self.ground_truth_records.append({
            "entity_id": id_b, 
            "anomaly_type": "DUPLICATE_APPLICATION", 
            "description": "Candidate recorded identical dual system pipeline entry tracking."
        })

        # --- Scenario C: Stage advanced bypassing mandatory verification checks ---
        r_c = dfs["job_requisitions"].iloc[1]["requisition_id"]
        c_c = dfs["candidates"].iloc[1]["candidate_id"]
        id_c, int_c = f"APP-{r_c}-{c_c}", "INT-2026-999002"
        dfs["applications"] = pd.concat([dfs["applications"], pd.DataFrame([{
            "application_id": id_c, 
            "requisition_id": r_c, 
            "candidate_id": c_c,
            "status": "OFFER_EXTENDED", 
            "applied_date": datetime.datetime(2026, 2, 1)
        }])], ignore_index=True)
        dfs["interviews"] = pd.concat([dfs["interviews"], pd.DataFrame([{
            "interview_id": int_c, 
            "application_id": id_c, 
            "interviewer_id": "INTV-000002",
            "scheduled_time": datetime.datetime(2026, 2, 5), 
            "round_number": 2
        }])], ignore_index=True)
        self.ground_truth_records.append({
            "entity_id": id_c, 
            "anomaly_type": "MISSING_FEEDBACK_STAGE_ADVANCED", 
            "description": "Workflow phase progressed bypassing core verification validation steps."
        })

        # --- Scenario D: Compensation structures violating budget rules ---
        req_d = dfs["job_requisitions"].iloc[2]
        id_d = f"APP-{req_d['requisition_id']}-{dfs['candidates'].iloc[2]['candidate_id']}"
        off_d = "OFF-2026-999001"
        bad_sal = float(req_d["max_salary"] + 65000.0)
        dfs["applications"] = pd.concat([dfs["applications"], pd.DataFrame([{
            "application_id": id_d, 
            "requisition_id": req_d['requisition_id'],
            "candidate_id": dfs['candidates'].iloc[2]['candidate_id'], 
            "status": "OFFER_EXTENDED",
            "applied_date": datetime.datetime(2026, 4, 1)
        }])], ignore_index=True)
        dfs["offers"] = pd.concat([dfs["offers"], pd.DataFrame([{
            "offer_id": off_d, 
            "application_id": id_d, 
            "salary_offered": bad_sal,
            "is_approved": True, 
            "status": "PENDING"
        }])], ignore_index=True)
        self.ground_truth_records.append({
            "entity_id": off_d, 
            "anomaly_type": "OFFER_SALARY_OUT_OF_BAND", 
            "description": f"Offered compensation metrics value completely violates requisition limits ({req_d['max_salary']})."
        })

        # --- Scenario E: Closed requisitions processing candidate flows ---
        cl_id = dfs["job_requisitions"][dfs["job_requisitions"]["status"] == "CLOSED"].iloc[0]["requisition_id"]
        id_e = f"APP-{cl_id}-{dfs['candidates'].iloc[3]['candidate_id']}"
        dfs["applications"] = pd.concat([dfs["applications"], pd.DataFrame([{
            "application_id": id_e, 
            "requisition_id": cl_id,
            "candidate_id": dfs['candidates'].iloc[3]['candidate_id'], 
            "status": "INTERVIEW_STAGE",
            "applied_date": datetime.datetime(2026, 5, 1)
        }])], ignore_index=True)
        self.ground_truth_records.append({
            "entity_id": cl_id, 
            "anomaly_type": "CLOSED_ROLE_ACTIVE_APPLICATIONS", 
            "description": "Dead job tracking index maintains active operational candidate routes."
        })

    def run_engine_pipeline(self) -> Dict[str, pd.DataFrame]:
        d, s = self.generate_master_directories()
        r = self.generate_job_requisitions(d)
        c, cs = self.generate_candidates(s)
        a, res = self.generate_applications(r, c)
        inv, i, f = self.generate_interviews_and_feedback(a)
        off = self.generate_offers(a, r)
        pkg = {
            "departments": d, "skills": s, "job_requisitions": r, "candidates": c, "candidate_skills": cs,
            "applications": a, "resume_artifacts": res, "interviewers": inv, "interviews": i, "feedback": f, "offers": off
        }
        self.inject_required_edge_scenarios(pkg)
        pkg["ground_truth"] = pd.DataFrame(self.ground_truth_records)
        return pkg


def verify_system_constraints(data: Dict[str, pd.DataFrame]) -> None:
    logger.info("Executing automated database primary-key and integrity validation loops...")
    assert data["job_requisitions"]["requisition_id"].is_unique, "PK failure: job_requisitions"
    assert data["candidates"]["candidate_id"].is_unique, "PK failure: candidates"
    assert data["applications"]["application_id"].is_unique, "PK failure: applications"
    assert data["applications"]["requisition_id"].isin(data["job_requisitions"]["requisition_id"]).all(), "FK failure: app -> req"
    assert data["applications"]["candidate_id"].isin(data["candidates"]["candidate_id"]).all(), "FK failure: app -> cand"
    logger.info("✅ Comprehensive relational schema constraint audits completed successfully.")


if __name__ == "__main__":
    root_target = "./"
    logger.info("Initiating Phase 10 Reproducibility Phase Verification Checks...")
    run1 = ATSDatasetGenerator(scale_factor=1.0, seed=20261022).run_engine_pipeline()
    run2 = ATSDatasetGenerator(scale_factor=1.0, seed=20261022).run_engine_pipeline()
    hash1 = {k: ATSDatasetGenerator.calculate_dataframe_checksum(v) for k, v in run1.items()}
    hash2 = {k: ATSDatasetGenerator.calculate_dataframe_checksum(v) for k, v in run2.items()}
    if hash1 == hash2:
        logger.info("⚡ Parity Check Passed: Data generator engine execution is completely deterministic.")
    else:
        raise AssertionError("Non-deterministic execution array parameters tracking anomalies.")
    verify_system_constraints(run1)
    logger.info("Exporting CSV seed data rows straight into workspace root folder array...")
    for name, df in run1.items():
        df.to_csv(os.path.join(root_target, f"{name}.csv"), index=False)
    logger.info("🏁 Challenge dataset generator run sequences executed perfectly!")

        




