CREATE TABLE "imovel"(
    "id" INTEGER NOT NULL,
    "tipo" TEXT NOT NULL,
    "cep" TEXT NOT NULL,
    "endereco" TEXT NOT NULL,
    "area" TEXT NOT NULL
);
ALTER TABLE
    "imovel" ADD PRIMARY KEY("id");
CREATE TABLE "cliente"(
    "id" INTEGER NOT NULL,
    "nome" TEXT NOT NULL,
    "documento" TEXT NOT NULL,
    "imoveis_proprios" TEXT NULL,
    "imovel_alugados" TEXT NULL
);
ALTER TABLE
    "cliente" ADD PRIMARY KEY("id");
CREATE TABLE "contrato"(
    "id" INTEGER NOT NULL,
    "locador" INTEGER NOT NULL,
    "locatario" INTEGER NOT NULL,
    "imovel_contratado" INTEGER NOT NULL,
    "vigencia_contrato" TEXT NOT NULL,
    "termos" TEXT NOT NULL
);
ALTER TABLE
    "contrato" ADD PRIMARY KEY("id");
ALTER TABLE
    "contrato" ADD CONSTRAINT "contrato_locador_foreign" FOREIGN KEY("locador") REFERENCES "cliente"("id");
ALTER TABLE
    "contrato" ADD CONSTRAINT "contrato_locatario_foreign" FOREIGN KEY("locatario") REFERENCES "cliente"("id");
ALTER TABLE
    "contrato" ADD CONSTRAINT "contrato_imovel_contratado_foreign" FOREIGN KEY("imovel_contratado") REFERENCES "imovel"("id");