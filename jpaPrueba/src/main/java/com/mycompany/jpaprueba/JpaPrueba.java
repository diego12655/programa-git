package com.mycompany.jpaprueba;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.EntityManager;

@SpringBootApplication
public class JpaPrueba {

    public static void main(String[] args) {
        SpringApplication.run(JpaPrueba.class, args);
    }
}

@Service
class MiServicio {

    private final EntityManager entityManager;

    @Autowired
    public MiServicio(EntityManager entityManager) {
        this.entityManager = entityManager;
    }

    @Transactional
    public void hacerAlgoConMiEntidad() {
        MiEntidad miEntidad = new MiEntidad();
        miEntidad.setNombre("Mi nombre");
        entityManager.persist(miEntidad);
    }
}

@Entity
class MiEntidad {

    @Id
    @GeneratedValue
    private Long id;

    private String nombre;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
}
