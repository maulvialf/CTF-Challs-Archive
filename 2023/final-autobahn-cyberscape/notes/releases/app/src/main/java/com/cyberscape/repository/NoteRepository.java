package com.cyberscape.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;

import com.cyberscape.model.Note;

public interface NoteRepository extends JpaRepository<Note, Long> {
    List<Note> findByIsPublic(boolean isPublic);

    List<Note> findByTitleContaining(String title);
}
