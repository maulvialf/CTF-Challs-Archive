package com.cyberscape;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.cyberscape.model.Note;
import com.cyberscape.repository.NoteRepository;

@SpringBootApplication
@RestController
public class Application {

    @Autowired
    NoteRepository noteRepository;

    @GetMapping("/")
    public ResponseEntity<List<Note>> home() {
        try {
            List<Note> notes = new ArrayList<Note>();

            noteRepository.findByIsPublic(true).forEach(notes::add);

            if (notes.isEmpty()) {
                return new ResponseEntity<>(HttpStatus.NO_CONTENT);
            }

            return new ResponseEntity<>(notes, HttpStatus.OK);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @PostMapping("/")
    public ResponseEntity<Note> createNote(@RequestBody Note note) {
        try {
            Note _note = noteRepository
                    .save(new Note(note.getTitle(), note.getContent(), true));
            return new ResponseEntity<>(_note, HttpStatus.CREATED);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @GetMapping(value = "/admin")
    public ResponseEntity<List<Note>> admin() {
        try {
            List<Note> notes = new ArrayList<Note>();

            noteRepository.findByIsPublic(false).forEach(notes::add);

            if (notes.isEmpty()) {
                return new ResponseEntity<>(HttpStatus.NO_CONTENT);
            }

            return new ResponseEntity<>(notes, HttpStatus.OK);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @PostMapping(value = "/admin")
    public ResponseEntity<Note> createAdminNote(@RequestBody Note note) {
        try {

            Note _note = noteRepository
                    .save(new Note(note.getTitle(), note.getContent(), false));
            return new ResponseEntity<>(_note, HttpStatus.CREATED);

        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
