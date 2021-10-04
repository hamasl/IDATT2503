FROM archlinux:latest
RUN pacman -Syu --noconfirm
RUN pacman -S clang --noconfirm
RUN pacman -S cmake --noconfirm
RUN pacman -S make --noconfirm
COPY . ./Task5
RUN cd Task5 && mkdir build && cd build && CC=clang cmake .. && make
CMD ["./Task5/build/tests/string_editor_fuzzer_test", "-max_total_time=60"]