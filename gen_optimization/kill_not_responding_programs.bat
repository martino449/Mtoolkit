@echo off
title kill_not_responding_programs - by Martin449
:i
taskkill /FI “STATUS eq NOT RESPONDING” /FI
goto i