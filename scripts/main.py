"""Main entry point for article generation."""

from generate_articles import generate_all, generate_search_pages


def main():
    print("=" * 60)
    print("Japan Travel Navi - Article Generator")
    print("=" * 60)

    print("\n[1/2] Generating articles for all spots x all languages...")
    count = generate_all()
    print(f"  -> Generated {count} articles.")

    print("\n[2/2] Generating search pages...")
    generate_search_pages()
    print("  -> Search pages created.")

    print("\n" + "=" * 60)
    print(f"Complete! {count} articles generated successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()
