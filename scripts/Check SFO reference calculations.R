# Independently verify headline Python references with tidyverse calculations in R.
# Run from the repository root with R 4.5+; install these packages if needed.
library(readr)
library(dplyr)
library(tidyr)
library(purrr)
library(jsonlite)

survey <- read_csv(
  "data/private/2018 SFO Customer Survey.csv",
  col_types = cols(.default = col_character()),
  na = character(),
  show_col_types = FALSE
)
names(survey) <- trimws(names(survey))
reference <- fromJSON("evaluation/reference/sfo-reference.json", simplifyVector = FALSE)

# Compute each 1-5 item on its own valid-answer base; retain actual row counts.
headline_fields <- c("Q7ALL", "Q7WIFI", "Q9Restroom")
results <- survey |>
  select(all_of(headline_fields), WEIGHT) |>
  mutate(WEIGHT = as.numeric(WEIGHT)) |>
  pivot_longer(all_of(headline_fields), names_to = "field", values_to = "code") |>
  mutate(rating = suppressWarnings(as.numeric(code))) |>
  filter(rating %in% 1:5) |>
  group_by(field) |>
  summarise(
    valid_n = n(),
    mean = mean(rating),
    weighted_mean = weighted.mean(rating, WEIGHT),
    happy_percent = mean(rating %in% c(4, 5)) * 100,
    weighted_happy_percent = weighted.mean(rating %in% c(4, 5), WEIGHT) * 100,
    .groups = "drop"
  )

# Compare each independently calculated field against the saved Python answer key.
walk(headline_fields, function(field_name) {
  actual <- results |> filter(field == field_name)
  unweighted <- reference$results[[paste0(field_name, ".unweighted")]]
  weighted <- reference$results[[paste0(field_name, ".weighted")]]
  stopifnot(
    actual$valid_n == unweighted$valid_n,
    abs(actual$mean - unweighted$mean) < 1e-10,
    abs(actual$weighted_mean - weighted$mean) < 1e-10,
    abs(actual$happy_percent - unweighted$top_two_percent) < 1e-10,
    abs(actual$weighted_happy_percent - weighted$top_two_percent) < 1e-10
  )
})

print(results, width = Inf)
cat("PASS: independent R checks of means, weighted means, percentages and n.\n")
