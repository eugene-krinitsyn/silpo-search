from dataclasses import dataclass
from Models.JSONModel import JSONModel


@dataclass
class Branch(JSONModel):
    branchId: str
    filialId: str | None
    companyId: str | None